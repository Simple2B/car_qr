document.addEventListener('DOMContentLoaded', function () {
    const dropZone = document.querySelector('#drop_zone');

    dropZone.addEventListener('dragover', function (e) {
        e.preventDefault();
        dropZone.style.backgroundColor = '#f7f7f7';
    });

    dropZone.addEventListener('dragleave', function (e) {
        e.preventDefault();
        dropZone.style.backgroundColor = '#fff';
    });

    dropZone.addEventListener('drop', function (e) {
        e.preventDefault();
        dropZone.style.backgroundColor = '#fff';

        const file = e.dataTransfer.files[0];
        var formData = new FormData();
        formData.append('file', file);

        var xhr = new XMLHttpRequest();
        xhr.open('POST', '/logo-upload/6ec64e2f-5bdf-4113-ae67-8809f97c41aa', true);
        xhr.onload = function () {
            if (xhr.status === 200) {
                alert('File uploaded successfully!');
            } else {
                alert('Error! Failed to upload the file.');
            }
        };
        xhr.send(formData);
    });
});