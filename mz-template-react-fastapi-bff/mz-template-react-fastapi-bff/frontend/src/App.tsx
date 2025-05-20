import { useState, useEffect } from 'react';
import { fetchConfig } from './api';
import ConfigDisplay from './components/ConfigDisplay';

function App() {
  const [config, setConfig] = useState<{
    entra_client_id?: string;
    entra_scope?: string;
    timestamp?: string;
    is_enabled?: boolean;
  } | null>(null);
  
  const [error, setError] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(true);

  useEffect(() => {
    // Fetch configuration from the API
    const loadConfig = async () => {
      try {
        setLoading(true);
        console.log('Starting to fetch config from API...');
        const configData = await fetchConfig();
        console.log('Config loaded successfully:', configData);
        setConfig(configData);
        setError(null);
      } catch (err: any) {
        const errorMessage = err?.message || 'Unknown error';
        console.error('Error loading config:', errorMessage);
        setError(`Failed to load configuration: ${errorMessage}`);
        setConfig(null);
      } finally {
        setLoading(false);
      }
    };

    loadConfig();
  }, []);

  return (
    <div className="app-container" style={{ 
      padding: '2rem',
      maxWidth: '800px',
      margin: '0 auto',
      fontFamily: 'system-ui, -apple-system, sans-serif'
    }}>
      <header>
        <h1>Secure Config Demo</h1>
        <p>This application demonstrates secure handling of configuration and API keys.</p>
      </header>

      <main>
        {loading && <p>Loading configuration...</p>}
        
        {error && (
          <div style={{ 
            padding: '1rem',
            backgroundColor: '#ffeeee',
            border: '1px solid #ffaaaa',
            borderRadius: '4px',
            marginTop: '1rem'
          }}>
            <strong>Error:</strong> {error}
          </div>
        )}

        {config && <ConfigDisplay config={config} />}
      </main>

      <footer style={{ 
        marginTop: '2rem',
        paddingTop: '1rem',
        borderTop: '1px solid #eee',
        fontSize: '0.8rem',
        color: '#666'
      }}>
        <p>Secure Config Management Example &copy; 2025</p>
      </footer>
    </div>
  );
}

export default App;