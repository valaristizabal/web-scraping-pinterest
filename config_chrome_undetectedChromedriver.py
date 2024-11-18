import undetected_chromedriver as uc

def iniciar_webdriver(headless=False, pos="maximizada"):
    #inicia el navegador de chrome y devuelve el objeto webdriver instanciado.
    #pos = indica la posición del navegador en la pantalla ("maximizada" | "izquierda" | "derecha").

    #instanciar options para las opciones de Chrome
    options = uc.ChromeOptions()
    #desactivar el guardado de credenciales
    options.add_argument("--password-store=basic")
    options.add_experimental_option(
        "prefs",{
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False 
        }
    )

    #instanciar webdriver
    driver = uc.Chrome(
        options=options,
        headless=headless,
        log_level=3,
    )
    #posicionar la ventana
    if not headless:
        driver.maximize_window()
        if pos != "maximizada":
            #obtener resolución de la ventana
            ancho, alto = driver.get_window_size().values()
            if pos == "izquierda":
                #posicionar la ventana en la mitad izquierda de la pantalla
                driver.set_window_rect(x=0,y=0,width=ancho//2, height=alto)
            elif pos == "derecha":
                driver.set_window_rect(x=ancho//2,y=0,width=ancho//2, height=alto)
    return driver
