import urllib2
'''
User-Agent : ��Щ�������� Proxy ��ͨ����ֵ���ж��Ƿ������������������
Content-Type : ��ʹ�� REST �ӿ�ʱ�������������ֵ������ȷ�� HTTP Body �е����ݸ�����������
������ȡֵ�У�
application/xml �� �� XML RPC���� RESTful/SOAP ����ʱʹ��
application/json �� �� JSON RPC ����ʱʹ��
application/x-www-form-urlencoded �� ������ύWeb��ʱʹ��
��ʹ�÷������ṩ�� RESTful �� SOAP ����ʱ�� Content-Type ���ô���ᵼ�·������ܾ�����
'''
request = urllib2.Request('http://www.baidu.com/')
request.add_header('User-Agent', 'fake-client')
response = urllib2.urlopen(request)
print response.read()
