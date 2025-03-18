import requests
from pyfiglet import Figlet
import folium
import sys

def get_info_by_ip(ip='127.0.0.1'):
	try:
		response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

		data = {
			'ip': response.get('query'),
			'провайдер': response.get('isp'),
			'организация': response.get('org'),
			'страна': response.get('country'),
			'имя региона': response.get('regionName'),
			'город': response.get('city'),
			'почтовый индекс': response.get('zip'),
			'широта': response.get('lat'),
			'долгота': response.get('lon'),
		}

		for k, v in data.items():
			print(f'{k} : {v}')

		area = folium.Map(location=[response.get('lat'), response.get('lon')])
		area.save(f'{response.get("query")}_{response.get("city")}.html')

	except requests.exceptions.ConnectionError:
		print('[!] Please check your connection!')


def main():
	preview_text = Figlet(font='slant')
	print(preview_text.renderText('STRIKERS'))
	try:
		ip = input('Enter IP> ')
		get_info_by_ip(ip=ip)
	except KeyboardInterrupt:
		print('\n[+] Cancellation...')


if __name__ == '__main__':
	main()
