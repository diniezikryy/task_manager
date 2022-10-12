import { useRouter } from "next/router";
import { useSelector } from "react-redux";
import Layout from "../hocs/Layout";

const Dashboard = () => {
  const router = useRouter();

  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const user = useSelector((state) => state.auth.user);
  const loading = useSelector((state) => state.auth.loading);

  if (typeof window !== "undefined" && !loading && !isAuthenticated)
    router.push("/login");

  return (
    <Layout
      title="httpOnly Auth | Dashboard"
      content="Dashboard page for httpOnly tutorial app"
    >
      <h1 className="text-green-500">Hello World</h1>
    </Layout>
  );
};

export default Dashboard;
