/* Runs in <head> before the page paints: marks JS as available and picks the language (closed list: es, en). */
document.documentElement.classList.remove('no-js');(function(){var l;try{l=new URLSearchParams(location.search).get('lang')||localStorage.getItem('lang')}catch(e){}if(l!=='es'&&l!=='en'){l='en'}document.documentElement.lang=l})();
