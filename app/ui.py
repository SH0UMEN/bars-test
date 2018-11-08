from objectpack.ui import BaseEditWindow
from m3_ext.ui import all_components as ext


class UserAddAndEditWindow(BaseEditWindow):
    def _init_components(self):
        super(UserAddAndEditWindow, self)._init_components()

        self.field__username = ext.ExtStringField(
            label=u'Имя пользователя',
            name='username',
            allow_blank=False,
            anchor='100%')

        self.field__lastname = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%')

        self.field__name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=True,
            anchor='100%')

        self.field__email = ext.ExtStringField(
            label=u'Email',
            name='email',
            allow_blank=True,
            anchor='100%')

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'Дата последнего входа',
            name='last_login',
            format='d.m.Y',
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'Дата регистрации',
            name='date_joined',
            format='d.m.Y',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Администратор',
            name='is_staff',
            anchor='100%')

        self.field__is_staff = ext.ExtCheckBox(
            label=u'Администратор',
            name='is_staff',
            anchor='100%')

        self.field__is_superuser = ext.ExtCheckBox(
            label=u'Все права',
            name='is_superuser',
            anchor='100%')

        self.field__is_active = ext.ExtCheckBox(
            label=u'Активен',
            name='is_active',
            anchor='100%')

        self.form.items.extend((
            self.field__username,
            self.field__email,
            self.field__lastname,
            self.field__name,
            self.field__password,
            self.field__last_login,
            self.field__date_joined,
            self.field__is_staff,
            self.field__is_superuser,
            self.field__is_active
        ))

    def _do_layout(self):
        super(UserAddAndEditWindow, self)._do_layout()
    def set_params(self, params):
        super(UserAddAndEditWindow, self).set_params(params)
        self.height = 'auto'