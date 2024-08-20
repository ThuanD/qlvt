from django.conf import settings
from django.contrib import admin
from django.utils.html import format_html
from django.utils.translation import gettext_lazy as _

from import_export import resources
from import_export.admin import ImportExportModelAdmin

from contract.models import Contract


class ContractResource(resources.ModelResource):

    class Meta:
        model = Contract


class ContractAdmin(ImportExportModelAdmin):
    list_display = ('id', 'name', 'contract', 'mtime')
    list_display_links = ('id', 'name')
    list_per_page = 20
    resource_classes = [ContractResource]

    def contract_tag(self, obj):
        return format_html(f'<img src = "{obj.contract.url}" width = "300"/>')
    contract_tag.short_description = _('Contract Tag')

    def qr_code(self, obj):
        string = f"""
        <div id="qrcode-{obj.id}"></div>
        <button style="
          background-color: var(--button-bg);
          border: none;
          color: var(--button-fg);
          padding: 7px;
          display: inline-block;
          cursor: pointer;
          transition: background 0.15s;
        " onclick="downloadQRCode('{obj.id}', '{obj.name}')">Download QR Code</button>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/qrcodejs/1.0.0/qrcode.min.js"></script>
        <script src="/static/qr_code.js"></script>
        <script type="text/javascript">
            makeQrCode({obj.id}, "{settings.SITE_URL}{obj.contract.url}");
        </script>
"""
        return format_html(string)
    qr_code.short_description = _('QR Code')

    fieldsets = (
        (
            _('Identity'),
            {
                'fields': ('name', )
            }
        ),
        (
            _('Media'),
            {
                'fields': ('contract', 'contract_tag', 'qr_code')
            }
        ),
    )
    readonly_fields = ('contract_tag', 'qr_code')


admin.site.register(Contract, ContractAdmin)
admin.site.index_title = _('QLTV')
admin.site.site_header = _('QLTV')
admin.site.site_title = _('Admin page')
admin.site.site_url = None
