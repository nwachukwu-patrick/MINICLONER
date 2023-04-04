# imported the requests library
import requests
image_folder = "C:\\Apache24\\fxiotex\\images"

image_list = [
 # 'Sergey.png',
'faq-token.png',
# 'faq-burn-drop.png',
# 'faq-journey.png',
# 'faq_platform.png',
# 'start_using_iotx.png',
# 'what_is_iotx.png',
# 'Giuseppe_Deluca.png',
# 'Gong.png',
# 'Hanna_Gan.png',

# 'Jack.png',
# 'Jing_c.png',
# 'Kate_Lifshits.png',
# 'Lori.png',
# 'Mariela_Tánchez.png',
# 'Mei.png',
# 'Michael.png',
# 'Olivier_Acuña.png',
# 'Raullen_c.png',
# 'RobertParker.jpeg',

    # 'Robert_Wolff.png',
    # 'Rynkiewicz.png',
    # 'Sergey.png',
    # 'Xinxin_c.png',
    # 'alexis_baydoun.png',
    # 'banner.png',
    # 'ben_clossey.png',
    # 'claire.png',
    # 'dustin.png',
    # 'harrison_wright.png',

]
for i in image_list:

        image_url = f'https://iotex.io/images/{i}'
        # URL of the image to be downloaded is defined as image_url
        r = requests.get(image_url)  # create HTTP response object

        # send a HTTP request to the server and save
        # the HTTP response in a response object called r
        with open(f'{image_folder}\\{i}', 'wb') as f:
            # Saving received content as a png file in
            # binary format

            # write the contents of the response (r.content)
            # to a new file in binary mode.
            f.write(r.content)


print("done...")
