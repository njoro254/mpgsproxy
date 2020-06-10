from base64 import b64encode
from Crypto.Hash import SHA256
from Crypto.Signature import PKCS1_v1_5
from Crypto.PublicKey import RSA


from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES, PKCS1_OAEP

from Crypto.Cipher import AES, PKCS1_OAEP




# signer and verifier to be called when signing strings to finserve and verifying signature from apps
def mySigner(concatenatedString):
	concatenatedString=str(concatenatedString)
	concatenatedStringUtf8encoded = concatenatedString.encode('utf-8')
	digester = SHA256.new()
	digester.update(concatenatedStringUtf8encoded)

	digest=digester.hexdigest()


	private_key = False

	with open("./mainModules/myCryptofunction/privatekey.pem", "r") as myfile:
	    private_key = RSA.importKey(myfile.read())

	signer = PKCS1_v1_5.new(private_key)
	sigBytes = signer.sign(digester)
	signBase64 = b64encode(sigBytes)

	#print (signBase64, digest)

	return digester, sigBytes


def myVerifier(digesterval, sigBytes):

	with open(u"./mainModules/myCryptofunction/publickey.pem", "r") as myfile:
	    public_key = RSA.importKey(myfile.read())

	verifier = PKCS1_v1_5.new(public_key)
	sigBytesNew = verifier.verify(digesterval, sigBytes)
	if sigBytesNew:
		message='successful verification'
		return message
	else:
		message='Verification failed'
		return message
	
	# assert, 'Signature verification failed'
	# print ("successful verification")




# digesterval=mySigner("twende")[0]
# sigBytes=mySigner("twende")[1]



# if myVerifier(digesterval, sigBytes)=='successful verification':
#         print('twende kass')
# elif myVerifier(digesterval, sigBytes)=='Verification failed':
#         print ('verification failed')
# else:
#         print ('unknown error')

