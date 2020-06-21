#https://dev.to/ezzy1337/a-pythonic-guide-to-solid-design-principles-4c8i


#the class to modify

class FTPClient:
  def __init__(self, **kwargs):
    self._ftp_client = FTPDriver(kwargs['host'], kwargs['port'])
    self._sftp_client = SFTPDriver(kwargs['sftp_host'], kwargs['user'], kwargs['pw'])

  def upload(self, file:bytes, **kwargs):
    is_sftp = kwargs['sftp']
    if is_sftp:
      with self._sftp_client.Connection() as sftp:
        sftp.put(file)
    else:
      self._ftp_client.upload(file)

  def download(self, target:str, **kwargs) -> bytes:
    is_sftp = kwargs['sftp']
    if is_sftp:
      with self._sftp_client.Connection() as sftp:
        return sftp.get(target)
    else:
      return self._ftp_client.download(target)


"""
SingleResposiblePrinciple(srp)

Every module/class should only have one responsibility and therefore only one reason to change.
The Single Responsibility Principle (SRP) is all about increasing cohesion and decreasing coupling by organizing code around responsibilities. It's not a big leap to see why that happens. If all the code for any given responsibility is in a single place that's cohesive and while responsibilities may be similar they don't often overlap. Consider this non-code example. If it is your responsibility to sweep and my responsibility to mop there's no reason for me to keep track of whether or not the floor has been swept. I can just ask you, "has the floor been swept"? and base my action according to your response.

Each use case should only be handled in one place, in turn, creating one obvious way to do things. This also satisfies the, "one reason to change" portion of the SRP's definition. The only reason this class should change is if the use case has changed.

Examining our original code we can see the class does not have a single responsibility because it has to manage connection details for an FTP, and SFTP server. Furthermore, the methods don't even have a single responsibility because both have to choose which protocol they will be using. This can be fixed by splitting the FTPClient class into 2 classes each with one of the responsibilities
"""
#modified after SRP

class FTPClient:
    def __init__(self, host, port):
        self._client = FTPDriver(host,port)

    def upload(self, file:bytes):
        self._client.upload(file)

    def download(self, target:str) -> bytes:
        return self._client.download(target)

class SFTPClient(FTPClient):
    def __init__(self, host, user, password):
        self._client = SFTPDriver(host, username=user, password=password)

    def upload(self, file:bytes):
        with self._client.Connection() as sftp:
            sftp.put(file)

    def download(self, target:str) -> bytes:
        with self._client.Connection() as sftp:
            return sftp.get(target)
"""
Opem Closed Principle (OCP)

Software Entities (classes, functions, modules) should be open for extension but closed to change

Since the definition of change and extension are so similar it is easy to get overwhelmed by the Open Closed Principle. I've found the most intuitive way to decide if I'm making a change or extension is to think about function signatures. A change is anything that forces calling code to be updated. This could be changing the function name, swapping the order of parameters, or adding a non-default parameter. Any code that calls the function would be forced to change in accordance with the new signature. An extension, on the other hand, allows for new functionality, without having to change the calling code. This could be renaming a parameter, adding a new parameter with a default value, or adding the *arg, or **kwargs parameters. Any code that calls the function would still work as originally written. The same rules apply to classes as well

Your gut reaction is probably to add a upload_bulk and download_bulk functions to the FTPClient class. Fortunately, that is also a SOLID way to handle this use case.
"""


class FTPClient:
    def __init__(self, host, port):
        self._client = FTPDriver(host,port)

    def upload(self, file:bytes):
        self._client.upload(file)

    def download(self, target:str) -> bytes:
        return self._client.download(target)

    def upload_bulk(self, files:List[str]):
        for file in files:
            self.upload(file)

    def download_bulk(self, targets:List[str]) -> List[bytes]:
        files = []
        for target in targets:
            files.append(self.download(target))

        return files
"""
it's better to extend the class with functions than extend through inheritance, because a BulkFTPClient child class would have to change the function signature for download reflecting it returns a list of bytes rather than just bytes, violating the Open Closed Principle as well as Liskov's Substituitability Principle.
"""


"""
Liskov's Substituitability Principle (LSP)
Definition: If S is a subtype of T, then objects of type T may be replaced with objects of Type S.

A plain English way of saying this is, "Any child class can replace its parent class without breaking functionality."
You may have noticed all of the FTP client classes so far have the same function signatures. That was done purposefully so they would follow Liskov's Substituitability Principle. An SFTPClient object can replace an FTPClient object and whatever code is calling upload, or download, is blissfully unaware.

Another specialized case of FTP file transfers is supporting FTPS (yes FTPS and SFTP are different). Solving this can be tricky because we have choices. They are:
1. Add upload_secure, and download_secure functions.
2. Add a secure flag through **kwargs.
3. Create a new class, FTPSClient, that extends FTPClient.

For reasons that we will get into during the Interface Segregation, and Dependency Inversion principles the new FTPSClient class is the way to go.
"""

class FTPSClient(FTPClient):
    def __init__(self, host, port, username, password):
        self._client = FTPSDriver(host, port, user=username, password=password)


"""
Interface Segregation Principle (ISP)
Definition: A client should not depend on methods it does not use.

ISP is about making reasonable choices for how other developers will interface with your code.A good interface will follow the semantics of the abstraction and match the terminology making the code more readable.

Let's look at how we can add an S3Client since it has the same upload/download semantics as the FTPClients. We want to keep the S3Clients signature for upload and download consistent, but it would be nonsense for the new S3Client to inherit from FTPClient. After all, S3 is not a special case of FTP. What FTP and S3 do have in common is that they are file transfer protocols and these protocols often share a similar interface as seen in this example. So instead of inheriting from FTPClient it would be better to tie these classes together with an abstract base class, the closest thing Python has to an interface.

We create a FileTransferClient which becomes our interface and all of our existing clients now inherit from that rather than inheriting from FTPClient. This forces a common interface and allows us to move bulk operations into their own interface since not every file transfer protocol will support them.

"""
from abc import ABC
class FileTransferClient(ABC):
  def upload(self, file:bytes):
    pass

  def download(self, target:str) -> bytes:
    pass

  def cd(self, target_dir):
    pass


class BulkFileTransferClient(ABC):
  def upload_bulk(self, files:List[bytes]):
    pass

  def download_bulk(self, targets:List[str]):
    pass

class FTPClient(FileTransferClient, BulkFileTransferClient):
    pass

class FTPSClient(FileTransferClient, BulkFileTransferClient):
    pass

class SFTPClient(FileTransferClient, BulkFileTransferClient):
    pass

class S3Client(FileTransferClient):
    pass

class SCPClient(FileTransferClient):
    pass


"""
Dependency Inversion Principle (DIP)
Definition: High-level modules should not depend on low-level modules. They should depend on abstractions and abstractions should not depend on details, rather details should depend on abstractions.

This is what ties it all together. Everything we've done with the other SOLID principles was to get to a place where we are no longer dependent on a detail, the underlying file transfer protocol, being used to move files around. We can now write code around our business rules without tying them to a specific implementation. Our code satisfies both requirements of dependency inversion.

Our high-level modules no longer need to depend on a low-level module like FTPClient, SFTPClient, or S3Client, instead, they depend on an abstraction FileTransferClient. We are depending on the abstraction of moving files not the detail of how those files are moved.

Our abstraction FileTransferClient is not dependent on protocol specific details and instead, those details depend on how they will be used through the abstraction (i.e. that files can be uploaded or downloaded).

Here is a example of Dependency Inversion at work.
"""

def exchange(client:FileTransferClient, to_upload:bytes, to_download:str) -> bytes:
    exchanger.upload(to_upload)
    return exchanger.download(to_download)

if __name__ == '__main__':
    ftp = FTPClient('ftp.host.com')
    sftp = FTPSClient('sftp.host.com', 22)
    ftps = SFTPClient('ftps.host.com', 990, 'ftps_user', 'P@ssw0rd1!')
    s3 = S3Client('ftp.host.com')
    scp = SCPClient('ftp.host.com')

    for client in [ftp, sftp, ftps, s3, scp]:
        exchange(client, b'Hello', 'greeting.txt')
    



  
