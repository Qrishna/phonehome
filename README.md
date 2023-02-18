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

# prerequisites
```shell
pip install -r requirements.txt
```

# to run the program
```
python phonehome.py
```

# to run the tests
```
pytest test-phonehome.py
```

#### references
#### 100% free and open source to get ip address information, gets ip address
#### You can use it without limit (even if you're doing millions of requests per minute.
https://www.ipify.org/ 

#### Free for non-commercial use, no API key required. Gets geolocation
### This endpoint is limited to 45 requests per minute from an IP address.

https://ip-api.com/

```text

# def registration():
# client side
# when the program starts attempt to first register the device
# if the device is already registered, phone home
# if the device is not registered, then register it and then  phone home

# django side
# done:: when the device is registered it should be set to Active False (Inactive from the admin page)
# done:: when the admin sets the device state to Active, then it can start receiving phone home events otherwise it can not

# done:: after the device is registered and set to active and a phone home event is received,the state of the device should be set to normal

# if the device's configs have been updated and the device has not phoned home and applied its configs yet,
# then its state should be set to pending

```


#### Thing API documentation
#### Create a new thing:
```shell

curl -X POST -H "Content-Type: application/json" -d '{"macaddress": "f4:5c:89:b4:b4:c7", "hostname": "JungBahadurs-MacBook-Pro.local", "active": "True"}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname":"Eleanores-MacBook-Pro.local","macaddress":"e4:5f:5e:72:3f:3b","public_ip":"128.12.147.238","ip":"192.168.1.101","platform":"darwin","network":{"interfaces":{"lo0":[{"address":"127.0.0.1","netmask":"255.0.0.0","broadcast":null},{"address":"::1","netmask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","broadcast":null},{"address":"fe80::1%lo0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en0":[{"address":"192.168.1.101","netmask":"255.255.255.0","broadcast":"192.168.1.255"},{"address":"fe80::1c10:9e9e:80f2:4a4d%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:6c50:7500:11a7:81a1:1796:82d0:26b6","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:6c50:7500:11a7:1cad:1819:fa29:8ddc","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en2":[],"en1":[],"bridge0":[],"p2p0":[],"awdl0":[{"address":"fe80::7c:63ff:fe99:157c%awdl0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"llw0":[{"address":"fe80::7c:63ff:fe99:157c%llw0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun0":[{"address":"fe80::11b9:fb15:b73e:146f%utun0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun1":[{"address":"fe80::bc8:df21:be37:28de%utun1","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun2":[{"address":"fe80::a86a:b300:f53d:74d9%utun2","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}]}},"info":{"geo_location":{"city":"San Francisco","region":"California","country":"United States","latitude":37.7749,"longitude":-122.4194},"release":"21.8.0","total_memory":8589934592,"cpu_info":{"frequency":"1.4 GHz","cores":4,"threads":8},"version":"Darwin Kernel Version 21.8.0: Thu Oct 20 16:04:41 PDT 2022; root:xnu-8019.141.1~1/RELEASE_X86_64","uptime":87695}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname":"My-MacBook-Air.local","macaddress":"4e:23:86:9e:6f:2a","public_ip":"72.229.28.185","ip":"192.168.1.100","platform":"darwin","network":{"interfaces":{"lo0":[{"address":"127.0.0.1","netmask":"255.0.0.0","broadcast":null},{"address":"::1","netmask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","broadcast":null},{"address":"fe80::1%lo0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en0":[{"address":"192.168.1.100","netmask":"255.255.255.0","broadcast":"192.168.1.255"},{"address":"fe80::6e23:86ff:fe9e:6f2a%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}]}},"info":{"geo_location":{"city":"New York","region":"New York","country":"United States","latitude":40.7128,"longitude":-74.006},"release":"20.6.0","total_memory":8589934592,"cpu_info":{"frequency":"1.6 GHz","cores":2,"threads":4},"version":"Darwin Kernel Version 20.6.0: Mon Aug 30 08:41:56 PDT 2021; root:xnu-7195.141.6~3/RELEASE_X86_64","uptime":208732}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname": "Robertos-MacBook-Air.local", "macaddress": "a0:45:89:27:f8:2a", "public_ip": "78.42.87.115", "ip": "192.168.1.12", "platform": "darwin", "network": {"interfaces": {"lo0": [{"address": "127.0.0.1", "netmask": "255.0.0.0", "broadcast": null}, {"address": "::1", "netmask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", "broadcast": null}, {"address": "fe80::1%lo0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "en0": [{"address": "192.168.1.12", "netmask": "255.255.255.0", "broadcast": "192.168.1.255"}, {"address": "fe80::f6:8b6:11b6:7e56%en0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}, {"address": "2a02:c7f:3e3d:f200:f694:1621:3d49:3a98", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}, {"address": "2a02:c7f:3e3d:f200:3042:49f0:b424:1b87", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}]}, "en2": [], "en1": [], "bridge0": [], "p2p0": [], "awdl0": [{"address": "fe80::abe1:5ff:fef5:b77%awdl0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "llw0": [{"address": "fe80::abe1:5ff:fef5:b77%llw0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "utun0": [{"address": "fe80::5a5f:1911:47a2:8be5%utun0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}]}, "info": {"geo_location": {"city": "Toronto", "region": "Ontario", "country": "Canada", "latitude": 43.651070, "longitude": -79.347015}, "release": "21.7.0", "total_memory": 8589934592, "cpu_info": {"frequency": "1.4 GHz", "cores": 2, "threads": 4}, "version": "Darwin Kernel Version 21.7.0: Mon Sep 26 19:41:50 PDT 2022; root:xnu-8019.101.1~1/RELEASE_X86_64", "uptime": 21856}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname": "Lanas-MacBook-Pro.local", "macaddress": "52:54:00:7d:08:1d", "public_ip": "174.101.192.221", "ip": "192.168.1.25", "platform": "darwin", "network": {"interfaces": {"lo0": [{"address": "127.0.0.1", "netmask": "255.0.0.0", "broadcast": null}, {"address": "::1", "netmask": "ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff", "broadcast": null}, {"address": "fe80::1%lo0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "en0": [{"address": "192.168.1.25", "netmask": "255.255.255.0", "broadcast": "192.168.1.255"}, {"address": "fe80::dfed:85ff:feb2:d59b%en0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}, {"address": "2601:245:4000:af80:dfed:85ff:feb2:d59b", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}, {"address": "2601:245:4000:af80:cc17:23d1:f35c:b55e", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "en2": [], "en1": [], "bridge0": [], "p2p0": [], "awdl0": [{"address": "1c:36:bb:8b:47:61", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "utun0": [{"address": "fe80::5a5b:f2b2:88b8:fe24%utun0", "netmask": "ffff:ffff:ffff:ffff::", "broadcast": null}], "utun1": [], "utun2": []}}, "info": {"geo_location": {"city": "Rochester", "region": "New York", "country": "United States", "latitude": 43.168, "longitude": -77.614}, "release": "21.5.0", "total_memory": 8589934592, "cpu_info": {"frequency": "2.4 GHz", "cores": 2, "threads": 4}, "version": "Darwin Kernel Version 21.5.0: Thu Nov 11 06:51:00 PST 2021; root:xnu-8019.123.7~2/RELEASE_ARM64_T8101", "uptime": 20010}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname":"Zoeys-MacBook-Pro.local","macaddress":"68:14:01:29:2e:e5","public_ip":"24.57.101.163","ip":"192.168.1.12","platform":"darwin","network":{"interfaces":{"lo0":[{"address":"127.0.0.1","netmask":"255.0.0.0","broadcast":null},{"address":"::1","netmask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","broadcast":null},{"address":"fe80::1%lo0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en0":[{"address":"192.168.1.12","netmask":"255.255.255.0","broadcast":"192.168.1.255"},{"address":"fe80::e4:3b43:4d4d:ad2%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"fe80::88d:39c0:818c:e381%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"fe80::92b2:cb8e:f123:9c50%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en2":[],"en1":[],"bridge0":[],"p2p0":[],"awdl0":[{"address":"fe80::d08b:a5ff:feb5:aec9%awdl0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"llw0":[{"address":"fe80::d08b:a5ff:feb5:aec9%llw0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun0":[{"address":"fe80::ad34:ee4:49a4:1084%utun0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun1":[],"utun2":[],"utun3":[],"utun4":[],"utun5":[],"utun6":[],"utun7":[]}},"info":{"geo_location":{"city":"New York","region":"New York","country":"United States","latitude":40.7306,"longitude":-73.9352},"release":"21.6.0","total_memory":8589934592,"cpu_info":{"frequency":"2.4 GHz","cores":4,"threads":8},"version":"Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64","uptime":259843}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname":"Shannons-MacBook-Pro.local","macaddress":"1c:1b:0d:8c:88:7b","public_ip":"184.2.186.33","ip":"192.168.1.101","platform":"darwin","network":{"interfaces":{"lo0":[{"address":"127.0.0.1","netmask":"255.0.0.0","broadcast":null},{"address":"::1","netmask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","broadcast":null},{"address":"fe80::1%lo0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en0":[{"address":"192.168.1.101","netmask":"255.255.255.0","broadcast":"192.168.1.255"},{"address":"fe80::3a7f:77c3:b081:e1d3%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:1700:7b70:4c60:8821:ccf4:977f:4c91","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:1700:7b70:4c60:3a7f:77c3:b081:e1d3","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en2":[],"en1":[],"bridge0":[],"p2p0":[],"awdl0":[{"address":"fe80::69be:12ff:fe1b:9c9f%awdl0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"llw0":[{"address":"fe80::69be:12ff:fe1b:9c9f%llw0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun0":[{"address":"fe80::d015:2315:5e5e:b120%utun0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun1":[{"address":"fe80::f03d:59b0:f5b3:35a3%utun1","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun2":[{"address":"fe80::515a:fe48:76b5:5b5a%utun2","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}]}}, "info":{"geo_location":{"city":"Omaha","region":"Nebraska","country":"United States","latitude":41.2565,"longitude":-95.9345},"release":"21.6.0","total_memory":8589934592,"cpu_info":{"frequency":"2.2 GHz","cores":4,"threads":8},"version":"Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64","uptime":93853}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname":"Mannus.Ubuntu","macaddress":"1d:1b:0d:8c:88:5b","public_ip":"194.21.186.33","ip":"192.168.1.112","platform":"linux","network":{"interfaces":{"lo0":[{"address":"127.0.0.1","netmask":"255.0.0.0","broadcast":null},{"address":"::1","netmask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","broadcast":null},{"address":"fe80::1%lo0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en0":[{"address":"192.168.1.101","netmask":"255.255.255.0","broadcast":"192.168.1.255"},{"address":"fe80::3a7f:77c3:b081:e1d3%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:1700:7b70:4c60:8821:ccf4:977f:4c91","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:1700:7b70:4c60:3a7f:77c3:b081:e1d3","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en2":[],"en1":[],"bridge0":[],"p2p0":[],"awdl0":[{"address":"fe80::69be:12ff:fe1b:9c9f%awdl0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"llw0":[{"address":"fe80::69be:12ff:fe1b:9c9f%llw0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun0":[{"address":"fe80::d015:2315:5e5e:b120%utun0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun1":[{"address":"fe80::f03d:59b0:f5b3:35a3%utun1","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun2":[{"address":"fe80::515a:fe48:76b5:5b5a%utun2","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}]}}, "info":{"geo_location":{"city":"Denver","region":"Colorado","country":"United States","latitude":39.7392,"longitude":-104.9903},"release":"21.6.0","total_memory":8589934592,"cpu_info":{"frequency":"2.2 GHz","cores":4,"threads":8},"version":"Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64","uptime":93853}}' http://localhost:8000/things
curl -X POST -H "Content-Type: application/json" -d '{"hostname":"Taras.Linux.local","macaddress":"2c:1b:0d:8c:88:8b","public_ip":"124.21.186.33","ip":"192.168.1.121","platform":"linux","network":{"interfaces":{"lo0":[{"address":"127.0.0.1","netmask":"255.0.0.0","broadcast":null},{"address":"::1","netmask":"ffff:ffff:ffff:ffff:ffff:ffff:ffff:ffff","broadcast":null},{"address":"fe80::1%lo0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en0":[{"address":"192.168.1.101","netmask":"255.255.255.0","broadcast":"192.168.1.255"},{"address":"fe80::3a7f:77c3:b081:e1d3%en0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:1700:7b70:4c60:8821:ccf4:977f:4c91","netmask":"ffff:ffff:ffff:ffff::","broadcast":null},{"address":"2600:1700:7b70:4c60:3a7f:77c3:b081:e1d3","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"en2":[],"en1":[],"bridge0":[],"p2p0":[],"awdl0":[{"address":"fe80::69be:12ff:fe1b:9c9f%awdl0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"llw0":[{"address":"fe80::69be:12ff:fe1b:9c9f%llw0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun0":[{"address":"fe80::d015:2315:5e5e:b120%utun0","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun1":[{"address":"fe80::f03d:59b0:f5b3:35a3%utun1","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}],"utun2":[{"address":"fe80::515a:fe48:76b5:5b5a%utun2","netmask":"ffff:ffff:ffff:ffff::","broadcast":null}]}}, "info":{"geo_location":{"city":"Seattle","region":"Washington","country":"United States","latitude":47.6062,"longitude":-122.3321},"release":"21.6.0","total_memory":8589934592,"cpu_info":{"frequency":"2.2 GHz","cores":4,"threads":8},"version":"Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64","uptime":93853}}' http://localhost:8000/things

```

#### Retrieve all things:
```shell
curl -s http://localhost:8000/things | python -m json.tool
```

#### Retrieve a specific thing by ID:
```shell
curl -s http://localhost:8000/things/1 | python -m json.tool
```

#### Update a specific thing by ID:
```shell
curl -X PUT -H "Content-Type: application/json" -d '{"id":1,"macaddress":"31:83:52:5a:e9:9L","hostname":"manjusapkota.com","orientation":"","state":"","dns":"","platform":"macos","network":"","config": "broken","type": "mannuri","taste": "amili","ip":"","label":"","info":"","placement":"","last_contact_action":"","location":2}' http://localhost:8000/things/1
```

#### Phone Home Events
```text

curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 2, "token": "24acf3b1c36f4ca6928cec39d718df40e7b4a9ef0b6d862b45d568d4f6647236", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 6962831360, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 129989, "load_average": [2.3984375, 2.21484375, 2.2548828125], "disk_space": {"free": 795286036480}, "policy_execution_results": null}}''
curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 3, "token": "a06d6b947b42ac323190ce0a8cf794e4975845dcb1608cb46578715ca7605914", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 7013773312, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130304, "load_average": [2.92578125, 2.5224609375, 2.36865234375], "disk_space": {"free": 795276541952}, "policy_execution_results": null}}'
curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 4, "token": "ef55b83638d3d68d5ce646e8854b3b510fa5a5bfdd3a824b2d24ac35359527e5", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 7015202816, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130374, "load_average": [2.43505859375, 2.45654296875, 2.35205078125], "disk_space": {"free": 795277950976}, "policy_execution_results": null}}'

curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 5, "token": "e99fa3b77ac71b5159516352c6ec734a5b952860e1dc2e4f636e9628a32f814e", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 7051460608, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130512, "load_average": [2.35546875, 2.388671875, 2.33447265625], "disk_space": {"free": 795273994240}, "policy_execution_results": null}}'
curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 6, "token": "da38660e0c8ecf8671ea6dc64738bb303547109dd1c6b922d33b98a05d0369a4", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 6979887104, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130576, "load_average": [2.30029296875, 2.38037109375, 2.33251953125], "disk_space": {"free": 795272491008}, "policy_execution_results": null}}'
curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 7, "token": "270a1de2b6c233c06c9644d181ed5d9f1846c15ce72190f3ac55a731702da19f", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 6984564736, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130577, "load_average": [2.30029296875, 2.38037109375, 2.33251953125], "disk_space": {"free": 795272491008}, "policy_execution_results": null}}'
curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 8, "token": "ea87f8fc138dbe0093c2b0009852a34ce68e9f846ddafdfa412771c6888e7f53", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 6984564736, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130577, "load_average": [2.30029296875, 2.38037109375, 2.33251953125], "disk_space": {"free": 795272523776}, "policy_execution_results": null}}'
curl -X POST http://localhost:8000/phonehome/ -H 'Content-Type: application/json' -d '{"thing_id": 9, "token": "fff93b218c7a712efb5f503da8768775ca373baf5e7f41488ff05a05cdf51d73", "message": {"ip_address": "192.168.0.23", "public_ip": "68.116.145.93", "geo_location": {"city": "Fort Worth", "region": "Texas", "country": "United States", "latitude": 32.7463, "longitude": -97.267}, "release": "21.6.0", "free_memory": 7000481792, "version": "Darwin Kernel Version 21.6.0: Wed Aug 10 14:25:27 PDT 2022; root:xnu-8020.141.5~2/RELEASE_X86_64", "uptime": 130578, "load_average": [2.30029296875, 2.38037109375, 2.33251953125], "disk_space": {"free": 795272491008}, "policy_execution_results": null}}'



```