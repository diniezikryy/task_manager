import "../styles/globals.css";

import Head from "next/head";
import { Provider } from "react-redux";
import { useStore } from "../store";
import { QueryClient, QueryClientProvider } from "@tanstack/react-query";

const App = ({ Component, pageProps }) => {
  const store = useStore(pageProps.initialReduxState);
  const queryClient = new QueryClient();

  return (
    <Provider store={store}>
      <QueryClientProvider client={queryClient}>
        <Head>
          <title>HTTPOnly Auth</title>
          <meta name="viewport" content="width=device-width, inital-scale=1" />
          <link rel="preconnect" href="https://fonts.googleapis.com" />
          <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
          <link
            href="https://fonts.googleapis.com/css2?family=Neucha&family=Plus+Jakarta+Sans:wght@200;300;400;500;600;700;800&display=swap"
            rel="stylesheet"
          ></link>
        </Head>
        <Component {...pageProps} />
      </QueryClientProvider>
    </Provider>
  );
};

export default App;
