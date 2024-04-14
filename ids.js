async function extrairIDsDasPaginas() {
    const ids = []; // Array para armazenar os IDs

    try {
        // Função para extrair IDs de uma página
        async function extrairIDsDaPagina(url) {
            const response = await fetch(url);
            const htmlString = await response.text();
            const parser = new DOMParser();
            const doc = parser.parseFromString(htmlString, 'text/html');
            const tdElements = doc.querySelectorAll('.Border td');
            tdElements.forEach(function (td) {
                const id = td.getAttribute('id');
                if (id && id.startsWith('info_')) {
                    ids.push(id.replace('info_', '')); // Remove "info_" e armazena o ID no array
                }
            });
        }

        // Função para gerar URL com base no número da página
        function gerarURLPagina(numeroPagina) {
            return `transfer-market.php?action=advancedsearchsubmit&position=100&rating=&lowervalue=0&highervalue=60000&lowerage=15&higherage=50&nationality=ANY&lowerrating=60&higherrating=99&fa=0&start=${(numeroPagina - 1) * 50 + 1}&offset=${(numeroPagina - 1) * 50}`;
        }

        // Loop para extrair IDs de cada página de 2 a 100
        for (let i = 0; i <= 40; i++) {
            const url = gerarURLPagina(i);
            await extrairIDsDaPagina(url);
            console.log(i);
        }

        // Após extrair todos os dados, exporta para um arquivo CSV
        exportarIDsParaCSV(ids);
    } catch (error) {
        console.error('Ocorreu um erro ao extrair IDs das páginas:', error);
    }
}

// Função para exportar IDs para um arquivo CSV
function exportarIDsParaCSV(ids) {
    // Cria o conteúdo do CSV
    const csvContent = ids.join(", "); // Altera a separação para vírgula e espaço

    // Cria um blob com o conteúdo CSV
    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });

    // Cria um link para download do arquivo CSV
    const link = document.createElement("a");
    if (link.download !== undefined) {
        const url = URL.createObjectURL(blob);
        link.setAttribute("href", url);
        link.setAttribute("download", "ids.csv");
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link);
    }
}

// Chama a função para extrair IDs de todas as páginas
extrairIDsDasPaginas();
