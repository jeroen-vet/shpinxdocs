odoo.define('sphinxdocs.UserMenu', function (require) {

var web_usermenu = require('web.UserMenu');

web_usermenu.include({
    _onMenuUserdocs: function() {
        window.open('/sphinxdocs/static/index.html', '_blank');
    },
    });
});
