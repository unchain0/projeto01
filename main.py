from fpdf import FPDF


def coletar_dados() -> tuple[str, str, str, str]:
    """
    Coleta informações do usuário sobre um projeto.

    :return: Uma tupla contendo as informações do projeto.
    """
    projeto = input("Digite a descrição do projeto: ")
    horas_previstas = input("Digite a quantidade de horas previstas: ")
    valor_hora = input("Digite o valor da hora trabalhada: ")
    prazo = input("Digite o prazo estimado: ")

    return projeto, horas_previstas, valor_hora, prazo


def gerar_pdf(projeto: str, horas_previstas: str, valor_hora: str, prazo: str) -> None:
    """
    Este método gera um documento PDF com as informações do projeto e salva como "Orçamento.pdf".

    O nome do projeto, horas estimadas, taxa horária, prazo e custo total são adicionados ao documento PDF.

    O custo total é calculado multiplicando as horas estimadas pela taxa horária.

    :param projeto: A descrição do projeto.
    :param horas_previstas: Quantidade de horas previstas.
    :param valor_hora: Valor da hora trabalhada.
    :param prazo: Prazo estimado.
    """
    valor_total = int(horas_previstas) * float(valor_hora)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial")
    pdf.image("template.png", 0, 0)

    x_text_start = 115
    text_spacing = 15
    pdf.text(x_text_start, 145, projeto)
    pdf.text(x_text_start, 145 + text_spacing, horas_previstas)
    pdf.text(x_text_start, 145 + text_spacing * 2, valor_hora)
    pdf.text(x_text_start, 145 + text_spacing * 3, prazo)
    pdf.text(x_text_start, 145 + text_spacing * 4, str(valor_total))

    pdf.output("Orçamento.pdf")
    print("Orçamento gerado com sucesso.")


try:
    projeto, horas_previstas, valor_hora, prazo = coletar_dados()
    gerar_pdf(projeto, horas_previstas, valor_hora, prazo)
except ValueError:
    print("Falha ao gerar o orçamento.")
