import React from 'react';

type ConfigDisplayProps = {
  config: {
    entra_client_id?: string;
    entra_scope?: string;
    timestamp?: string;
    is_enabled?: boolean;
  };
};

const ConfigDisplay: React.FC<ConfigDisplayProps> = ({ config }) => {
  return (
    <div style={{
      backgroundColor: '#f9f9f9',
      border: '1px solid #ddd',
      borderRadius: '8px',
      padding: '1.5rem',
      marginTop: '1.5rem',
    }}>
      <h2>Configuration Values</h2>
      <p>
        These values were securely fetched from the backend API using a runtime-injected API key.
      </p>

      <div style={{
        backgroundColor: '#fff',
        border: '1px solid #eee',
        borderRadius: '4px',
        padding: '1rem',
        fontFamily: 'monospace',
        marginTop: '1rem',
      }}>
        <pre style={{ margin: 0, overflow: 'auto' }}>
          {JSON.stringify(config, null, 2)}
        </pre>
      </div>

      <div style={{ marginTop: '1.5rem' }}>
        <h3>Details</h3>
        <table style={{ width: '100%', borderCollapse: 'collapse' }}>
          <tbody>
            <tr>
              <td style={{ padding: '0.5rem', borderBottom: '1px solid #eee', fontWeight: 'bold' }}>
                Entra Client ID
              </td>
              <td style={{ padding: '0.5rem', borderBottom: '1px solid #eee' }}>
                <code className="code">{config.entra_client_id || 'Not available'}</code>
              </td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem', borderBottom: '1px solid #eee', fontWeight: 'bold' }}>
                Entra Scope
              </td>
              <td style={{ padding: '0.5rem', borderBottom: '1px solid #eee' }}>
                <code className="code">{config.entra_scope || 'Not available'}</code>
              </td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem', borderBottom: '1px solid #eee', fontWeight: 'bold' }}>
                Timestamp
              </td>
              <td style={{ padding: '0.5rem', borderBottom: '1px solid #eee' }}>
                {config.timestamp || 'Not available'}
              </td>
            </tr>
            <tr>
              <td style={{ padding: '0.5rem', fontWeight: 'bold' }}>
                Enabled
              </td>
              <td style={{ padding: '0.5rem' }}>
                {config.is_enabled !== undefined ? String(config.is_enabled) : 'Not available'}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default ConfigDisplay;