try:
    import vk_api
    login = input('Введите логин: ')
    pwd = input('Введите пароль: ')
    with open('VKBotToken.txt', 'w') as file:
        VkAPI = vk_api.VkApi(login, pwd)
        VkAPI.auth()
        file.write(VkAPI.token['access_token'])
    print("Ваш E-Mail: %s;\nСсылка на Ваш аккаунт: https://vk.com/id%s" % (VkAPI.token['email'], VkAPI.token['user_id']))
except Exception as err:
    print("ОШИБКА! (%s): %s\nПожалуйста, повторите попытку." % (type(err).__name__, err))
