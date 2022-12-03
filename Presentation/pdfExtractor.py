import os
import fitz


def extract():
    workdir = "content"  # directory where content's are stored
    dest = "images"

    try:
        os.mkdir(str(dest))
    except:
        print('', end='')

    for each_path in os.listdir("content"):
        if ".pdf" in each_path:
            doc = fitz.Document((os.path.join(workdir, each_path)))

            for i in range(len(doc)):
                for img in doc.get_page_images(i):
                    print(img)
                    xref = img[0]
                    image = doc.extract_image(xref)
                    pix = fitz.Pixmap(doc, xref)
                    pix.save(os.path.join(dest, "%s_p%s-%s.png" % (each_path[:-4], i, xref)))


    print("Done!")


extract()