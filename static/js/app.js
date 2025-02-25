
document.addEventListener('DOMContentLoaded', function() {
    const imgContainer = document.getElementById('imageContainer');

    if(!sessionStorage.getItem('pageLoaded')) {
        imgContainer.style.display = 'none';
    }
    sessionStorage.setItem('pageLoaded', 'True');
});

document.getElementById('fileInput').addEventListener('change', function(event) {
    const input = event.target;
    const preview = document.getElementById('imagePreview');
    const imgContainer = document.getElementById('imageContainer');
    const uploadContainer = document.getElementById('uploadContainer');

    if (input.files && input.files[0]) {
      const reader = new FileReader();

      reader.onload = function(e) {
        preview.src = e.target.result;
        preview.style.display = 'block';
        imgContainer.style.display = 'flex';
        uploadContainer.style.display = 'none';

        sessionStorage.setItem('uploadedImage', e.target.result);
    };

      reader.readAsDataURL(input.files[0]);
    } else {
        preview.src = '#';
        preview.style.display = 'none';
        imgContainer.style.display = 'none';
        uploadContainer.style.display = 'block';

        sessionStorage.removeItem('uploadedImage');
    }
});

// window.addEventListener('load', function() {
//     const preview = document.getElementById('imagePreview');
//     const upload = document.getElementById('uploadArea');
//     const imgContainer = document.getElementById('imageContainer');
//     const savedImage = sessionStorage.getItem('uploadedImage');

//     if (savedImage) {
//         preview.src = savedImage;
//         preview.style.display = 'block';
//         upload.style.display = 'none';
//         imgContainer.style.display = 'flex';
//     }
// });
