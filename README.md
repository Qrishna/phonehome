#### phonehome



#### CERTIFICATES
```
# full_chain.pem

When you obtain a certificate from Let's Encrypt, it typically consists of three separate certificates combined into a single file called fullchain.pem. These three certificates are:

Domain Certificate: 
This is the main certificate for your domain, also known as the end-entity certificate. 
It contains information about your domain name, expiration date, and public key. 
This certificate is used to establish a secure connection between your server and the client's browser.

Intermediate Certificate: 
This is the certificate that chains your domain certificate to Let's Encrypt's root certificate.
It serves as a middleman between the two, and helps to establish trust in the certificate chain. 
This certificate is also known as the chain certificate.

Root Certificate: 
This is the top-level certificate in the certificate hierarchy, and it's the certificate that ultimately establishes the trust in the certificate chain.
This certificate is issued by Let's Encrypt's certificate authority and is already trusted by most web browsers and operating systems.

All three certificates are necessary for your certificate to be valid and trusted by clients. 
The domain certificate is what establishes the identity of your domain, while the intermediate and root certificates establish trust in the certificate chain. 
When a client connects to your server, it checks the entire certificate chain to make sure that each certificate is valid and trusted. If any of the certificates in the chain are invalid or untrusted, the connection will fail.
```

#### certificate files
```
# ca.pem 
The ca.pem file contains the public key certificates of the Certificate Authorities (CAs) that are trusted to verify the server's certificate.

If the server's certificate is issued by a well-known public CA, then the ca.pem file is usually provided by the CA. For example, you can obtain the ca.pem file for Let's Encrypt from the following URL:

https://letsencrypt.org/certs/isrgrootx1.pem.txt
If the server's certificate is issued by a private CA, then the ca.pem file can be obtained from the organization that operates the private CA. The private CA's root certificate must be installed on the client's machine in order to verify the server's certificate.

# In SSL/TLS communication, the certificate is used to authenticate the server to the client and establish a secure connection. The certificate is a digital document that contains information about the identity of the server, the public key of the server, and the digital signature of the certificate authority that issued the certificate.

# cert.pem
The cert.pem file typically contains the X.509 certificate for the server, which includes the public key of the server. The public key is a cryptographic key that is used to encrypt data that can only be decrypted by the corresponding private key, which is kept secret by the server.

# key.pem
The key.pem file typically contains the private key of the server, which is used to decrypt data that was encrypted with the public key. The private key must be kept secure and should never be shared with anyone.

# info
In SSL/TLS communication, the server sends its certificate to the client during the initial handshake. The client verifies the certificate by checking the digital signature and the identity of the certificate authority that issued the certificate. If the certificate is valid, the client uses the public key in the certificate to encrypt a random symmetric key that is used to encrypt the data being sent between the client and the server. The server uses its private key to decrypt the symmetric key, and then uses the symmetric key to encrypt and decrypt the data being sent.

To summarize, the cert.pem file contains the X.509 certificate for the server, which includes the public key of the server. The key.pem file contains the private key of the server, which is used to decrypt data that was encrypted with the public key.
```

# to run the program
python phonehome.py

# to run the tests
pytest test-phonehome.py
