window.onload = function () {
    /*
    // можем получить DOM-объект меню через JS
    var menu = document.getElementsByClassName('menu')[0];
    menu.addEventListener('click', function () {
        console.log(event);
        event.preventDefault();
    });
    
    // можем получить DOM-объект меню через jQuery
    $('.menu').on('click', 'a', function () {
        console.log('event', event);
        console.log('this', this);
        console.log('event.target', event.target);
        event.preventDefault();
    });
   
    // получаем атрибут href
    $('.menu').on('click', 'a', function () {
        var target_href = event.target.href;
        if (target_href) {
            console.log('нужно перейти: ', target_href);
        }
        event.preventDefault();
    });
    */
    
    // добавляем ajax-обработчик для обновления количества товара
    $('.basket_list').on('click', 'input[type="number"]', function (event) {

        //console.log('Привет');
        //alert('ПРивет');
        var target_href = event.target;

        if (target_href) {
        // Пример отправки ajax запроса
            $.ajax({
                url: "/basket/edit/" + target_href.name + "/" + target_href.value + "/",
                // method: 'post',
                //data: {'param': 'pampam'}
                success: function (data) {
                    $('.basket_list').html(data.result);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });


    $('.basket_list').on('click', '.btn-round', function (event) {

        //console.log('Привет');
        //alert('ПРивет');
        var target_href = event.target;

        if (target_href) {
        // Пример отправки ajax запроса
            $.ajax({
                url: "/basket/ajaxdelete/" + target_href.name + "/",
                // method: 'post',
                //data: {'param': 'pampam'}
                success: function (data) {
                    $('.basket_list').html(data['result']);
                    console.log('ajax done');
                },
            });

        }
        event.preventDefault();
    });
}