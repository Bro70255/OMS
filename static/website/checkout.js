$('.addtocartBtn').click(function (e){
    e.preventDefault();

    var product_id=$(this).closest('.product_data').find(".prod_id").val();
    var token = $('input[name=csrfmiddlewaretoken]'),val();

    $.ajax({
        method: "POST",
        url: "checkout",
        data: {
          "product_id":product_id,
          csrfmiddlewaretoken: token
        },
        dataType: "dataType",
        success: function(response){
        }
    })
})