"use strict";

$('#upload-item-form').on('submit', (evt) => {
    evt.preventDefault();
    console.log(evt)
    const form_data = new FormData();
    form_data.append('file', $('#image-field').prop('files')[0]);
    form_data.append('image_name', $('#name-field').val());
    form_data.append('image_description', $('#description-field').val());
    console.log(form_data)

    $.ajax({
        type: 'POST',
        url: '/newimage',
        data: form_data,
        contentType: false,
        cache: false,
        processData: false,
        success: (res) => {
            const image = res;
            const new_image = (
                `<div class="card mb-3" style="max-width: 540px;">
                    <form method="POST" id="upload-item" >
                        <div class="row no-gutters">
                            <div class="col-md-6">
                                <img src="${image.image_url}" class="card-img-top">
                            </div>
                            <div class="col-md-6">
                                <div class="card-body">
                                    <p class="card-text">
                                        <b>Item Name: </b>${image.image_name}
                                        <b>Description: </b>${image.image_description}
                                        <br>
                                    </p>
                                </div>
                            </div>
                        </div>
                    </form>
                </div>`
            );
            $('#image-library').prepend(new_item)
        },
    });
});

const searchInput = document.querySelector('#search input');
const searchIcon = document.querySelector('#search svg');

searchInput.onkeyup = (event) => {
  if (event.keyCode === 13) {
    openSearchPage();
  }
};

searchIcon.onclick = openSearchPage;

function openSearchPage() {
  const query = searchInput.value;
    // document.location.href = `/search/${query}`;
  alert(query);
}