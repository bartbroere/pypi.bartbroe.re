  async function main() {
    let pyodide = await loadPyodide({ indexURL : "https://bartbroere.eu/pyodide.bartbroe.re/build/" });
    for (const element of document.querySelectorAll('script[type="text/x-python"]')) {
      await pyodide.loadPackagesFromImports(element.text);
      console.log(pyodide.runPython(element.text));
    }
  }
  function waitForPyodide(){
    if(typeof loadPyodide !== "undefined"){
      main();
    }
    else{
      setTimeout(waitForPyodide, 250);
    }
  }
  script = document.createElement("script");
  script.src = "https://bartbroere.eu/pyodide.bartbroe.re/build/pyodide.js";
  document.head.appendChild(script);
  waitForPyodide();
