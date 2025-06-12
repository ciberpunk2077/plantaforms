var clearButton = document.querySelector("[data-action=clear]");
var savePNGButton = document.querySelector("[data-action=save-png]");

function download(dataURL, filename) {
  if (navigator.userAgent.indexOf("Safari") > -1 && navigator.userAgent.indexOf("Chrome") === -1) {
    window.open(dataURL);
  } else {
    var blob = dataURLToBlob(dataURL);
    var url = window.URL.createObjectURL(blob);

    var a = document.createElement("a");
    a.style = "display: none";
    a.href = url;
    a.download = filename;

    document.body.appendChild(a);
    a.click();

    window.URL.revokeObjectURL(url);
  }
}

// One could simply use Canvas#toBlob method instead, but it's just to show
// that it can be done using result of SignaturePad#toDataURL.
function dataURLToBlob(dataURL) {
  // Code taken from https://github.com/ebidel/filer.js
  var parts = dataURL.split(';base64,');
  var contentType = parts[0].split(":")[1];
  var raw = window.atob(parts[1]);
  var rawLength = raw.length;
  var uInt8Array = new Uint8Array(rawLength);

  for (var i = 0; i < rawLength; ++i) {
    uInt8Array[i] = raw.charCodeAt(i);
  }

  return new Blob([uInt8Array], { type: contentType });
}

clearButton.addEventListener("click", function (event) {
  signaturePad.clear();
});


savePNGButton.addEventListener("click", function (event) {
  if (signaturePad.isEmpty()) {
    alert("Firma no captada.");
  } else {
    var dataURL = signaturePad.toDataURL();
    document.getElementById('messages').innerHTML = (`<h4 class="text-success"><i class="fa fa-certificate"></i> Se ha generado un idenficador único de la firma</h4><hr><span class="alert alert-success">  ${dataURL.slice(20,200)} </span>`)
    document.querySelector('#firma').value=dataURL;
    var previewZone = document.querySelectorAll(`span.${variableFirma}`);
    for (let i = 0; i < previewZone.length; i++) {
        let img=document.createElement('img');
        img.src=dataURL;
        img.style.width="200px"
        previewZone[i].innerHTML = ''
        previewZone[i].appendChild(img);
    }
  }
});