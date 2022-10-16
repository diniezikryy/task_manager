import "../styles/globals.css";
import "tailwindcss/tailwind.css";

import Head from "next/head";
import { Provider } from "react-redux";
import { useStore } from "../store";
import {
  QueryClient,
  QueryClientProvider,
  useQuery,
} from "@tanstack/react-query";

const App = ({ Component, pageProps }) => {
  const store = useStore(pageProps.initialReduxState);
  const queryClient = new QueryClient();

  return (
    <Provider store={store}>
      <QueryClientProvider client={queryClient}>
        <Head>
          <title>HTTPOnly Auth</title>
          <meta name="viewport" content="width=device-width, inital-scale=1" />
        </Head>
        <Component {...pageProps} />
      </QueryClientProvider>
    </Provider>
  );
};

export default App;
