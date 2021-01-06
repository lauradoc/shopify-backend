"use strict";

$.get('/', (res) => {
    const images = res;
    for (const image of images) {
        const imageDetails = (
            `<ul>
                <img src="${image.image_url}" class="img-thumbnail">
            </ul>`
        );
        $('#image-library').append(imageDetails);
    };
});