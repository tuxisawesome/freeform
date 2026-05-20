(() => {
  const setThemeByTime = () => {
    const hour = new Date().getHours();
    // Enable dark mode if it's before 6 AM or after 6 PM
    const theme = (hour < 6 || hour >= 18) ? 'dark' : 'light';
    
    document.documentElement.setAttribute('data-bs-theme', theme);
  };

  setThemeByTime();
})();
