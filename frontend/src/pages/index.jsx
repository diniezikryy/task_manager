import Head from "next/head";

const homePage = () => {
  return (
    <div>
      <Head>
        <title>Kanban App | Home</title>
        <meta name="viewport" content="initial-scale=1.0, width=device-width" />
      </Head>

      <div>
        <h1>Welcome to Kanban App</h1>
      </div>
    </div>
  );
};

export default homePage;
