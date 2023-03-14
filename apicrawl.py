import requests

cookies = {
    'visitor_id': '35a2ef7c-c899-4e12-8800-ccb174116565',
    'x-available-eg': 'ecom',
    '__zlcmid': '1EkleNehpBAL82x',
    'RT': '"z=1&dm=noon.com&si=od6yrbif9os&ss=lf0nqsez&sl=1&tt=0&nu=70d6d009fb3e2ddb8b35021dc8d8822b&cl=1tc3j&obo=1&ld=1vuts&r=70d6d009fb3e2ddb8b35021dc8d8822b&ul=1vutv&hd=1vuu6"',
    'x-available-ae': 'ecom-daily',
    'AKA_A2': 'A',
    'ak_bmsc': '46FF21131B6560B9C8B16DAC5373E4BB~000000000000000000000000000000~YAAQLzZ8aBQ+S8OGAQAAqLUqyxO3eZ07f5+kDl19VEihB9nPGPojCZmpZM6DMrhI2uzAvV29H6Hbc4bKgAERKgeqOWQyNxCFS2yBQQJ9JAwPVxBiNKdTafKkraID5g9b2zDZYEYj1gKs9TxHV/puaeNY/CaBHCHH721Tz0lJdatRx0DEJTj9K+Y/JZiLtaREqxXw4fqDtdf9JQZBh4rCUQoWCvP+9FP85hJc+29DQSBs8kUVeroGmIl3cV1V3XpH85eygFxYf/gtqrXOT5k8OtgLqzgQx3ny5SKDaY01RyP8IcXMwk8Aaz0mAly2PhbgGFVcDddE1HZYX2+wbTzOe4jIzopv7wlcgGrb8ctadBzooIaGXqIiY25jokQUJaWD7FoIBB18PESjug==',
    'nguest': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lKbU56QTFOMk0wT0RjMk5qWTBNVE5rT1RobE5qY3lNV0ppTmpnelltSTRPQ0lzSW1saGRDSTZNVFkzT0RBNU5UWTNPWDAuQ1kycjVRa0NSMkZZZzltV2RXMEY5WEtFYUctZUlndGlPOEdyY2ZtTVhLNCIsImlhdCI6MTY3ODQ0NTgyNX0.h0jZsn5EdHAfhPBNv9Tfd2GVyiedHZt3SDsfRUFtgaI',
    '_nsc': 'nsv1.public.eyJzdGlkIjoiZGI4MDljYWEtZWMxYi00MzMwLTkwY2UtNzc3Nzk0NWIyYWY4Iiwic2lkIjoiZjcwNTdjNDg3NjY2NDEzZDk4ZTY3MjFiYjY4M2JiODgiLCJpYXQiOjE2Nzg0NDU4MjUsInZpZCI6IjM1YTJlZjdjLWM4OTktNGUxMi04ODAwLWNjYjE3NDExNjU2NSIsImhvbWVwYWdlIjp7fX0xdVA4VWhvYVRBWWx2RDlvakxxMTNONzZsbTU5cmNnT3dBQ2R6VnZPTVl3PQ.MQ',
    'bm_mi': 'E18B12972B213A04E07FC971767E0A6F~YAAQMFstF6vDM76GAQAARRkryxMup/bPO2XwJJrun6V+3X3mBRtu2NMHWz4EwEJKa6APXTCEGRR5hcGBzZwhO34K3ttNdIF1BLCRyla8i3cIb6kWyuMDVwD7DvLnlnvF/OnMkVGjWf6ecga+rqU6pF2T8mvkrE1PtPNBIFTg8spxE+3rusJYQDjHn1CVgf04X9G+W6DAEyrea/iU55uciQf9CDwC+fI0l0w+QX2Yvk9HYPd2uYeomZ+H0+xIKLsiqtxhEfzYo5pYVWD1o+o1PPLOw93ROtwtPTDYfTUnOGL2/pKm/HN1LZ7wSvKUiod2HiY=~1',
    'bm_sv': 'ACDB21B16A8334189DD10EBDF9757273~YAAQMFstFxHFM76GAQAAFlcryxO/W4GlQTejHA5AkJ1qywqti70yfSHcUopQmM4sRt4lA+8H+gpaLm2UHZi8VGje7YtMAmm2qc3jjdxU+qsB9OLTW9fOFZnKpiQaWORUtseU5Vtu4t54LFm02M2ehONPP90StuJODewkEjVHxBOu1FEvPIv055SnMoaLPXNOpjPpEjnKs9glHBXsdMk8hBqULw7wZcrP7FDFvlNdMo3De+tddzL2NFTVNmQZ/fQ=~1',
}

headers = {
    'authority': 'www.noon.com',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9,hi;q=0.8',
    # 'cookie': 'visitor_id=35a2ef7c-c899-4e12-8800-ccb174116565; x-available-eg=ecom; __zlcmid=1EkleNehpBAL82x; RT="z=1&dm=noon.com&si=od6yrbif9os&ss=lf0nqsez&sl=1&tt=0&nu=70d6d009fb3e2ddb8b35021dc8d8822b&cl=1tc3j&obo=1&ld=1vuts&r=70d6d009fb3e2ddb8b35021dc8d8822b&ul=1vutv&hd=1vuu6"; x-available-ae=ecom-daily; AKA_A2=A; ak_bmsc=46FF21131B6560B9C8B16DAC5373E4BB~000000000000000000000000000000~YAAQLzZ8aBQ+S8OGAQAAqLUqyxO3eZ07f5+kDl19VEihB9nPGPojCZmpZM6DMrhI2uzAvV29H6Hbc4bKgAERKgeqOWQyNxCFS2yBQQJ9JAwPVxBiNKdTafKkraID5g9b2zDZYEYj1gKs9TxHV/puaeNY/CaBHCHH721Tz0lJdatRx0DEJTj9K+Y/JZiLtaREqxXw4fqDtdf9JQZBh4rCUQoWCvP+9FP85hJc+29DQSBs8kUVeroGmIl3cV1V3XpH85eygFxYf/gtqrXOT5k8OtgLqzgQx3ny5SKDaY01RyP8IcXMwk8Aaz0mAly2PhbgGFVcDddE1HZYX2+wbTzOe4jIzopv7wlcgGrb8ctadBzooIaGXqIiY25jokQUJaWD7FoIBB18PESjug==; nguest=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJyIjoiZXlKaGJHY2lPaUpJVXpJMU5pSXNJblI1Y0NJNklrcFhWQ0o5LmV5SnJhV1FpT2lKbU56QTFOMk0wT0RjMk5qWTBNVE5rT1RobE5qY3lNV0ppTmpnelltSTRPQ0lzSW1saGRDSTZNVFkzT0RBNU5UWTNPWDAuQ1kycjVRa0NSMkZZZzltV2RXMEY5WEtFYUctZUlndGlPOEdyY2ZtTVhLNCIsImlhdCI6MTY3ODQ0NTgyNX0.h0jZsn5EdHAfhPBNv9Tfd2GVyiedHZt3SDsfRUFtgaI; _nsc=nsv1.public.eyJzdGlkIjoiZGI4MDljYWEtZWMxYi00MzMwLTkwY2UtNzc3Nzk0NWIyYWY4Iiwic2lkIjoiZjcwNTdjNDg3NjY2NDEzZDk4ZTY3MjFiYjY4M2JiODgiLCJpYXQiOjE2Nzg0NDU4MjUsInZpZCI6IjM1YTJlZjdjLWM4OTktNGUxMi04ODAwLWNjYjE3NDExNjU2NSIsImhvbWVwYWdlIjp7fX0xdVA4VWhvYVRBWWx2RDlvakxxMTNONzZsbTU5cmNnT3dBQ2R6VnZPTVl3PQ.MQ; bm_mi=E18B12972B213A04E07FC971767E0A6F~YAAQMFstF6vDM76GAQAARRkryxMup/bPO2XwJJrun6V+3X3mBRtu2NMHWz4EwEJKa6APXTCEGRR5hcGBzZwhO34K3ttNdIF1BLCRyla8i3cIb6kWyuMDVwD7DvLnlnvF/OnMkVGjWf6ecga+rqU6pF2T8mvkrE1PtPNBIFTg8spxE+3rusJYQDjHn1CVgf04X9G+W6DAEyrea/iU55uciQf9CDwC+fI0l0w+QX2Yvk9HYPd2uYeomZ+H0+xIKLsiqtxhEfzYo5pYVWD1o+o1PPLOw93ROtwtPTDYfTUnOGL2/pKm/HN1LZ7wSvKUiod2HiY=~1; bm_sv=ACDB21B16A8334189DD10EBDF9757273~YAAQMFstFxHFM76GAQAAFlcryxO/W4GlQTejHA5AkJ1qywqti70yfSHcUopQmM4sRt4lA+8H+gpaLm2UHZi8VGje7YtMAmm2qc3jjdxU+qsB9OLTW9fOFZnKpiQaWORUtseU5Vtu4t54LFm02M2ehONPP90StuJODewkEjVHxBOu1FEvPIv055SnMoaLPXNOpjPpEjnKs9glHBXsdMk8hBqULw7wZcrP7FDFvlNdMo3De+tddzL2NFTVNmQZ/fQ=~1',
    'referer': 'https://www.noon.com/uae-en/playstation-5-console-disc-version-with-controller/N40633047A/p/?o=f1a1763f22ab6e6b',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
    'x-aby': '{"ipl.enabled":1,"ipl_entrypoint.enabled":1,"navpills_with_icons.navpills_with_icons":true,"noon_pass.enabled":1,"recommendations.recommendations_pdp_toggle":1,"show_ar_model.enabled":1,"wishlist_experiment_entrypoint.entry_point_wishlist":2,"wishlist_toggle.wishlist_toggle":true,"wishlist_toggle_v2.enabled":true}',
    'x-cms': 'v3',
    'x-content': 'desktop',
    'x-lat': '25.1998495',
    'x-lng': '55.2715985',
    'x-locale': 'en-ae',
    'x-mp': 'noon',
    'x-platform': 'web',
    'x-visitor-id': '35a2ef7c-c899-4e12-8800-ccb174116565',
}

params = {
    'o': 'f1a1763f22ab6e6b',
}

response = requests.get(
    'https://www.noon.com/_svc/catalog/api/v3/u/playstation-5-console-disc-version-with-controller/N40633047A/p/',
    params=params,
    cookies=cookies,
    headers=headers,
)
res = response.json()
print(res['meta']['h1'])