import React, { useEffect } from 'react';

export default function App() {
  useEffect(() => {
    window.location.href = '/amazon.html?v=' + new Date().getTime();
  }, []);

  return (
    <div className="flex items-center justify-center min-h-screen">
      <p>Loading Amazon Giveaway Page...</p>
    </div>
  );
}
