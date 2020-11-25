from luxand import luxand

client = luxand("9c5fdf210f8e41a086b92d65508bc884")

result = client.detect(photo = "./test1.jpg")

print(result)