from pyrastreio import correios, jadlog, sequoia

print('Correios:')
print(correios('CODIGO_RASTREIO_CORREIOS'))
print('Jadlog:')
print(jadlog('CODIGO_RASTREIO_JADLOG'))
# sequoia precisa do cpf ou cnpj além do código de rastreio
print('Sequoia:')
print(sequoia('CODIGO_RASTREIO_SEQUOIA', '11111111111'))