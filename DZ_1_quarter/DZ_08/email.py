import re


def email_parse(email):
    a = re.findall(r'^\w+@\w+\.\w+', email)
    if a:
        pars = re.split('@', email)
        print({'username': pars[0], 'domen': pars[1]})
    else:
        raise ValueError(f'некорректный email:{email}')


email_parse('PutinPloxoy@EtoPravda.ru')
