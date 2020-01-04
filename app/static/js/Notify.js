Notify = function (text, style, time, callback, close_callback) {

    if (typeof time == 'undefined') time = 10000;
    var $container = $('#notifications');
    var icon = '<i class="fa fa-info-circle "></i>';

    if (typeof style == 'undefined') style = 'info';

    var html = $('<div class="alert alert-' + style + '  hide">' + icon + " " + text + '</div>');

    $('<a>', {
        text: '×',
        class: 'button close',
        style: 'padding-left: 10px;',
        href: '#',
        click: function (e) {
            e.preventDefault();
            close_callback && close_callback();
            remove_notice();
        }
    }).prependTo(html);

    $container.prepend(html);
    html.removeClass('hide').hide().fadeIn(700);

    function remove_notice() {
        html.stop().fadeOut(700, complete=(function () {
            html.remove();
        }));
    }

    var timer = setTimeout(remove_notice, time);

    $(html).hover(function () {
        clearInterval(timer);
    }, function () {
        timer = setTimeout(remove_notice, time);
    });

    html.on('click', function () {
        clearInterval(timer);
        callback && callback();
        remove_notice();
    });
};
