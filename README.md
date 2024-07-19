# sslcipherscan
Esse script tem por objetivo identificar cifras de SSL/TLS fracas.
Ele realiza diversos testes obtendo uma lista de conjuntos de cifras suportados pelo OpenSSL e tenta se conectar testando cada uma das cifras fracas ('RC4', 'MD5', 'SSLv2', 'EXP', 'NULL', 'ADH', 'LOW', '3DES', 'DES') 
Se o handshake for bem-sucedido, ele imprime YES. Se o handshake não for bem-sucedido, ele imprime NO.


Uso:
python3 sslcipherscan.py

Insira o endereço alvo(example.com:443):

![image](https://github.com/user-attachments/assets/257ecd90-aabc-434a-8cf4-cf983cae0bf1)


