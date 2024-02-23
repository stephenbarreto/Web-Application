export default function formatDate(dateString) {
  // Verifica se a string de data está no formato 'YYYY-MM-DD'
  if (!/^\d{4}-\d{2}-\d{2}$/.test(dateString)) {
    console.error("Formato de data inválido. Use o formato 'YYYY-MM-DD'.");
    return null;
  }

  // Divide a string da data em partes (ano, mês, dia)
  const parts = dateString.split('-');
  const year = parseInt(parts[0]);
  const month = parseInt(parts[1]);
  const day = parseInt(parts[2]);

  // Cria um objeto Date com a data
  const dateObject = new Date(year, month - 1, day);

  // Formata a data para o padrão brasileiro ('DD/MM/YYYY')
  const formattedDate = dateObject.toLocaleDateString('pt-BR');

  return formattedDate;
}
