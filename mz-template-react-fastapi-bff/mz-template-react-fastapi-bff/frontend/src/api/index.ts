/**
 * API client for interacting with the backend
 * 
 * This module handles all communication with the backend API,
 * including fetching the API key at runtime and using it for
 * authenticated requests.
 */

// Type for public config response
interface PublicConfig {
  apiKey: string;
}

// Type for protected config response
interface ProtectedConfig {
  entra_client_id: string;
  entra_scope: string;
  timestamp: string;
  is_enabled: boolean;
}

// Store the API key in memory (never in localStorage or cookies)
let apiKey: string | null = null;

/**
 * Fetch the public configuration including the API key
 */
export const fetchPublicConfig = async (): Promise<PublicConfig> => {
  try {
    console.log('Fetching public config from /config.json...');
    const response = await fetch('/config.json', {
      method: 'GET',
      headers: {
        'Accept': 'application/json',
        'Cache-Control': 'no-cache'
      }
    });
    
    if (!response.ok) {
      console.error(`Public config fetch failed: ${response.status} ${response.statusText}`);
      throw new Error(`Failed to fetch public config: ${response.status} ${response.statusText}`);
    }
    
    const data = await response.json();
    console.log('Public config fetched successfully');
    return data;
  } catch (error) {
    console.error('Error fetching public config:', error);
    throw error;
  }
};

/**
 * Get the API key, fetching it if not already loaded
 */
export const getApiKey = async (): Promise<string> => {
  // If we already have the API key in memory, return it
  if (apiKey) {
    return apiKey;
  }
  
  // Otherwise, fetch it from the public config endpoint
  const config = await fetchPublicConfig();
  apiKey = config.apiKey;
  
  if (!apiKey) {
    throw new Error('No API key found in config response');
  }
  
  return apiKey;
};

/**
 * Fetch the protected configuration data
 */
export const fetchConfig = async (): Promise<ProtectedConfig> => {
  // Get the API key (will be fetched if not already loaded)
  const key = await getApiKey();
  
  try {
    const response = await fetch('/api/config', {
      headers: {
        'Content-Type': 'application/json',
        'x-api-key': key
      }
    });
    
    if (!response.ok) {
      throw new Error(`Failed to fetch protected config: ${response.status} ${response.statusText}`);
    }
    
    return await response.json();
  } catch (error) {
    console.error('Error fetching protected config:', error);
    throw error;
  }
};