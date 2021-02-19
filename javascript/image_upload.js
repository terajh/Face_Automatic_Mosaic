// var myDropzone = new myDropzone("div#dZUpload",
// {
//     url: "/fileupload",
//     addRemoveLinks: true,
//     maxFiles: 5,
//     success: function(file, response) {
//         var imagName = response.serFileNm;
//         var oriName = response.orgFileNm;
//         if(imgName != ''){
//             var adClass = imgName.replace('.', "");
//             file.previewElement.classList.add("dz-success");
//             file.previewElement.classList.add(adClass);
//             var html = `<input type="hidden' name="serverFileNm" value
//                         ="${imgName}">`;
//             html += `<input type-"hidden" name="oriFileNm" value="${oriName}">`;
//             $("."+adClass).append(html); 
//         }
//     }, error: function(file, response) {
//         file.previewElement.classList.add("dz-maxsize-error");
//         alert("파일은 최대 5개까지만 업로드 가능합니다.");
//         $(".dz-maxsize-error").empty();
//     }
// })