from PIL import Image
im = Image.open("CaminhDaImagemNoPC.jpg")

nova_largura = 100
ratio = nova_largura / im.width
nova_altura = int(im.height * ratio)
imagem_ajustada = im.resize((nova_largura, nova_altura))

im_cinza = imagem_ajustada.convert("L")
pixels = list(im_cinza.getdata())

escala_ascii = "@%#*+=-:. "  # Do mais escuro ao mais claro
def pixel_ascii(brilho):
    indice = brilho / 255 * (len(escala_ascii) - 1)
    return escala_ascii[int(indice)]

ascii = []

for y in range(nova_altura):
    linha = [pixel_ascii(pixels[y * nova_largura + x]) for x in range(nova_largura)]
    ascii.append("".join(linha))
resultado = "\n".join(ascii)

print(resultado)  # Exibe diretamente no terminal