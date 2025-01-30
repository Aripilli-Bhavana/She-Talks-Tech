export const useApi = () => {
    const callApi = async (endpoint, method = 'GET', body = null) => {
      try {
        const response = await fetch(`/api/${endpoint}`, {
          method,
          headers: { 'Content-Type': 'application/json' },
          body: body ? JSON.stringify(body) : null
        });
        return await response.json();
      } catch (error) {
        return { error: "API Connection Failed" };
      }
    };
  
    return { callApi };
  };