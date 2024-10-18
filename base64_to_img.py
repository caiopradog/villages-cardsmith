import base64


def base64_to_img():
    file_path = "base_images/images.js"

    img_path = "base_images"
    with open(file_path) as file:
        lines = file.readlines()[2:-3]
        for line in lines:
            line = line.replace('\t', '') \
                       .replace('\n', '') \
                       .replace(' ', '') \
                       .replace("'", '')[:-1]
            try:
                (img_name, base64_img) = line.split(':', 1)

                with open(f"{img_path}/{img_name}.png", "wb") as fh:
                    img_data = base64_img.replace('data:image/png;base64,', '')
                    fh.write(base64.b64decode(img_data))
            except ValueError:
                print(line)
