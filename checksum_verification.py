'''
Verify checksum
TODO
Eventually add ability to just enter file path and what checksum should be and
this script will use certutil on its own
cmd syntax: certutil -hashfile path_here type (i.e. SHA256)
i.e. certutil -hashfile C:\Users\senoj\Downloads\debian-11.6.0-amd64-netinst.iso SHA512
'''

should_be = '224cd98011b9184e49f858a46096c6ff4894adff8945ce89b194541afdfd93b73b4666b0705234bd4dff42c0a914fdb6037dd0982efb5813e8a553d8e92e6f51'
result = '224cd98011b9184e49f858a46096c6ff4894adff8945ce89b194541afdfd93b73b4666b0705234bd4dff42c0a914fdb6037dd0982efb5813e8a553d8e92e6f51'

print(should_be == result)
