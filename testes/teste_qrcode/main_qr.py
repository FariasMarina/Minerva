import qrcode

data = input('Digite o que quer gravar em QR Code: ')
qr = qrcode.QRCode(version = 1, 
                   box_size = 10, 
                   border = 5) 

qr.add_data(data)

qr.make(fit = True) 
img = qr.make_image(fill_color = 'blue', 
                    back_color = 'white') 
  
img.save('Minerva_teste.png')