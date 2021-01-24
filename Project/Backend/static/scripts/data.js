$(function () {
    $('#toolbar').w2toolbar({
        name: 'toolbar',
        items: [
            { type: 'button', id: 'upload', text: 'Upload files', img: 'icon-page' }
        ],
        onClick: function (event) {
            if (event.target == 'upload'){
                $('#popup1').w2popup({
                    onClose: function(){
                        $('#w2ui-popup span').text('');
                    }
                });
            }
        }            
    });

    $('#grid').w2grid({ 
        name: 'grid', 
        searches: [                
            { field: 'fname', caption: 'First Name', type: 'text' },
            { field: 'lname', caption: 'Last Name', type: 'text' },
            { field: 'email', caption: 'Email', type: 'text' }
        ],
        sortData: [ { field: 'lname', direction: 'asc' } ],
        columns: [                
            { field: 'recid', caption: 'ID', size: '50px', sortable: true },
            { field: 'fname', caption: 'First Name', size: '30%', sortable: true },
            { field: 'lname', caption: 'Last Name', size: '30%', sortable: true },
            { field: 'email', caption: 'Email', size: '40%' },
            { field: 'sdate', caption: 'Start Date', size: '120px' }
        ],
        records: [
            { recid: 1, fname: 'John', lname: 'doe', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 2, fname: 'Stuart', lname: 'Motzart', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 3, fname: 'Jin', lname: 'Franson', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 4, fname: 'Susan', lname: 'Ottie', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 5, fname: 'Kelly', lname: 'Silver', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 6, fname: 'Francis', lname: 'Gatos', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 7, fname: 'Mark', lname: 'Welldo', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 8, fname: 'Thomas', lname: 'Bahh', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 9, fname: 'Sergei', lname: 'Rachmaninov', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 20, fname: 'Jill', lname: 'Doe', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 21, fname: 'Frank', lname: 'Motzart', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 22, fname: 'Peter', lname: 'Franson', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 23, fname: 'Andrew', lname: 'Ottie', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 24, fname: 'Manny', lname: 'Silver', email: 'jdoe@gmail.com', sdate: '4/3/2012' },
            { recid: 25, fname: 'Ben', lname: 'Gatos', email: 'jdoe@gmail.com', sdate: '4/3/2012' }
        ]
    });

    $(document).on('click', '#w2ui-popup button', function(event){
        const fileInputElement = $('#w2ui-popup input[type=file]')[0];
        const progressBar = $('#w2ui-popup .progress');
        const statusText = $('#w2ui-popup span');

        if(fileInputElement.files.length == 0) {
            alert('Error : No file selected');
            return;
        }

        let file = fileInputElement.files[0];
        let allowed_mime_types = [ 'text/csv' ];
        let allowed_size_mb = 2;
    
        if(allowed_mime_types.indexOf(file.type) == -1) {
            alert('Error : Incorrect file type');
            return;
        }

        if(file.size > allowed_size_mb*1024*1024) {
            alert('Error : Exceeded size');
            return;
        }

        let data = new FormData();
        Array.prototype.forEach.call(fileInputElement.files, function(file) { data.append('files[]', file) });

        let request = new XMLHttpRequest();
        request.open('POST', '/upload-bankstatements'); 

        // upload progress event
        request.upload.addEventListener('progress', function(e) {
            let percent_complete = (e.loaded / e.total)*100;
            
            progressBar.css("width", percent_complete);
            // percentage of upload completed
            console.log(percent_complete);
        });

        // AJAX request finished event
        request.addEventListener('load', function(e) {
            // HTTP status message
            console.log(request.status);
            progressBar.hide();

            if(request.status === 200){
                statusText.text('File(s) uploaded successfully.');
            }
            else{
                statusText.text('There was an error uploading file(s).');
            }

            // request.response will hold the response from the server
            console.log(request.response);

            fileInputElement.value = null;
        });

        progressBar.show();

        // send POST request to server side script
        request.send(data);
    });
});