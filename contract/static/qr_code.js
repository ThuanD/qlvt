function makeQrCode(id, message) {
  // Create the QR code
  new QRCode(
    document.getElementById("qrcode-" + id), {
      text: message,
      width: 300,
      height: 300,
      colorDark: "#000000",
      colorLight: "#ffffff",
      correctLevel: QRCode.CorrectLevel.H
    });

  let qrElement = document.getElementById("qrcode-" + id);
  let canvas = qrElement.querySelector('canvas');
  if (canvas) {
    let padding = 20;
    let paddedCanvas = document.createElement('canvas');
    let paddedContext = paddedCanvas.getContext('2d');

    paddedCanvas.width = canvas.width + (2 * padding);
    paddedCanvas.height = canvas.height + (2 * padding);

    paddedContext.fillStyle = "#ffffff";
    paddedContext.fillRect(0, 0, paddedCanvas.width, paddedCanvas.height);

    paddedContext.drawImage(canvas, padding, padding);

    let qrImageUrl = paddedCanvas.toDataURL('image/png');

    qrElement.innerHTML = `<img id="imgQR${id}" src="${qrImageUrl}" width="300" />`;
  }
}

function downloadQRCode(id, name) {
    let image = document.getElementById("imgQR" + id);

    if (image) {
        let link = document.createElement('a');
        link.href = image.src;
        link.download = name + '.png';
        document.body.appendChild(link); // Append to the body to make it work in some browsers
        link.click();
        document.body.removeChild(link); // Remove from the body after download
    }
}