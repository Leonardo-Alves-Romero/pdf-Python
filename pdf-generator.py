from reportlab.pdfgen import canvas


def GeneratePDF(lista):
    try:
        nome_pdf = input('informe o nome do PDF: ')
        pdf = canvas.canvas('{}.pdf'.format(nome_pdf))
        x = 720
        for nome, idade in lista.items():
            x -= 20
            pdf.drawString(247, x, '{} : {}'.format(nome, idade))
        pdf.setTitle(nome_pdf)
        pdf.setFont('Helvetica-oblique', 14)
        pdf.drawString(245, 750, 'Lista de clientes')
        pdf.setFont("Helvetica-bold", 12)
        pdf.drawString(245, 724, 'Nome e idade')
        pdf.save()
        print('{}.pdf criado com sucesso!'.format(nome_pdf))
    except:
        print('Erro ao gerar {}.pdf'.format(nome_pdf))


lista = {'Leonardo': '28', 'Mario': '32', 'Fernando': '30', 'Eduardo': '21'}

GeneratePDF(lista)
