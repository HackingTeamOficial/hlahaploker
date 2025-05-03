🚀 Herramienta de Automatización para Pentesting Web 🚀

Hola comunidad, quiero compartir con ustedes una herramienta que he desarrollado para facilitar y acelerar el proceso de reconocimiento y escaneo en pruebas de penetración web. Esta herramienta automatiza varias fases clave usando herramientas reconocidas en el mundo del hacking ético.
¿Qué hace esta herramienta?

    Realiza un escaneo inicial con nmap para identificar servicios y versiones.
    Recolecta URLs relevantes del objetivo usando gau, gauplus, hakrawler y waybackurls.
    Encuentra parámetros potenciales con ParamSpider.
    Combina y filtra URLs únicas para un análisis más eficiente.
    Verifica la disponibilidad y estado de las URLs con httpx.
    Realiza escaneos profundos con katana y nuclei para detectar vulnerabilidades.
    Ejecuta pruebas básicas de inyección SQL con sqlmap.
    Sugiere el uso manual de Metasploit para explotación avanzada.

¿Por qué es útil?

Esta herramienta centraliza y automatiza tareas que normalmente se hacen manualmente, ahorrando tiempo y asegurando que no se omitan pasos importantes en el reconocimiento. Además, guarda todos los resultados organizados en carpetas con timestamp para facilitar el análisis posterior.
¿Qué necesitas para usarla?

    Tener instaladas las herramientas mencionadas (nmap, gau, hakrawler, waybackurls, ParamSpider, httpx, katana, nuclei, sqlmap, Metasploit).
    Permisos y autorización para realizar pruebas en el dominio objetivo.
    Python 3 para ejecutar el script.

Ejemplo de uso

Solo ejecuta el script, introduce el dominio objetivo y deja que la herramienta haga el resto. Al finalizar, tendrás un conjunto completo de resultados para comenzar tu análisis de seguridad.

Proximamente se le integrara mas herramientas por parte de la comunidad Hacking Team lo cual Facilitara el mejor analisis automatizado y integracion de herramientas para tecnicas Osint
