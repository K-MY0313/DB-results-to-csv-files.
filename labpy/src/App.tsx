import React, { useState } from 'react';
import axios from 'axios';

const ExportComponent: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);

  const handleExport = async () => {
    setLoading(true);
    setError(null);
    try {
      const url = 'http://localhost:8000/export/csv';
      console.log(`Request URL: ${url}`); // デバッグログ
      const response = await axios.get(url, {
        responseType: 'blob',
      });
      
      const blob = new Blob([response.data], { type: 'text/csv' });
      const downloadUrl = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = downloadUrl;
      link.download = 'measurements.csv';
      document.body.appendChild(link);
      link.click();
      link.remove();
    } catch (error) {
      console.error('Export failed:', error);
      if (axios.isAxiosError(error) && error.response) {
        setError(`エクスポートに失敗しました: ${error.response.status} ${error.response.statusText}`);
      } else {
        setError('エクスポートに失敗しました。もう一度お試しください。');
      }
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <h1>Export Measurements</h1>
      <button onClick={handleExport} disabled={loading}>
        Export to CSV
      </button>
      {loading && <p>Exporting measurements...</p>}
      {error && <p style={{ color: 'red' }}>{error}</p>}
    </div>
  );
};

export default ExportComponent;