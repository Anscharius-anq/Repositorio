def remove_space(text: str, /) -> str:
    """
    Remueve todos los espacios de una cadena dada.
    """
    new_text = ""
    for char in text:
        if char != " ":
            new_text += char
    return new_text


def reverse(texto: str) -> str:
    """
    invierte los caracteris de una cadana.
    """
    reversed_text = ""
    for char in texto:
        reversed_text = char + reversed_text
    return reversed_text


def palindromo(texto: str) -> bool:
    """
    verifica si el texto dado es un palindromo
    """
    new_text = remove_space(texto.lower())
    reversed_text = reverse(new_text)
    return new_text == reversed_text

 
 
