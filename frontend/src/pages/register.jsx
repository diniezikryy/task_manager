import { useState } from "react";
import { useSelector, useDispatch } from "react-redux";
import { useRouter } from "next/router";
import { registerUser } from "../actions/auth";
import Layout from "../hocs/Layout";
import Loader from "react-loader-spinner";
import router from "next/router";
import Navbar from "../components/Navbar";
import { useForm } from "react-hook-form";
import Link from "next/link";

const RegisterPage = () => {
  const dispatch = useDispatch();
  const router = useRouter();
  const register_success = useSelector((state) => state.auth.register_success);
  const isAuthenticated = useSelector((state) => state.auth.isAuthenticated);
  const loading = useSelector((state) => state.auth.loading);

  const {
    register,
    handleSubmit,
    formState: { errors },
  } = useForm();

  const onSubmit = (data) => {
    console.log(data);
    if (dispatch && dispatch !== null && dispatch !== undefined)
      dispatch(
        registerUser(
          data.firstName,
          data.lastName,
          data.username,
          data.password,
          data.rePassword
        )
      );
  };

  if (typeof window !== "undefined" && isAuthenticated)
    router.push("/dashboard");

  if (register_success) router.push("/login");

  return (
    <Layout
      title="Kanban App | Login"
      content="Login page for kanban app login"
    >
      <Navbar />

      <div className="flex flex-col h-full">
        <div className="flex flex-col w-full p-6 m-auto sm:w-1/2 md:w-1/2 lg:w-1/2 my-28">
          <h2 className="mx-auto mb-10 text-3xl font-semibold">
            Register for an account
          </h2>
          <form onSubmit={handleSubmit(onSubmit)} className="w-full">
            <div className="mb-6">
              <label
                for="firstName"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                First Name
              </label>
              <input
                type="text"
                id="firstName"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="First Name"
                {...register("firstName", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.firstName && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>

            <div className="mb-6">
              <label
                for="lastName"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                Last Name
              </label>
              <input
                type="text"
                id="lastName"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="Last Name"
                {...register("lastName", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.lastName && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>

            <div className="mb-6">
              <label
                for="username"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                Username
              </label>
              <input
                type="text"
                id="username"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="Username"
                {...register("username", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.username && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>

            <div className="mb-6">
              <label
                for="password"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                Password
              </label>
              <input
                type="password"
                id="password"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="Password"
                {...register("password", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.password && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>

            <div className="mb-6">
              <label
                for="rePassword"
                className="block mb-2 text-sm font-medium text-purple-primary"
              >
                Re-enter Password
              </label>
              <input
                type="password"
                id="password"
                className="border border-grey-dark-primary text-grey-dark-primary placeholder-grey-light-tertiary text-sm rounded-lg focus:ring-purple-primary focus:border-purple-primary block w-full p-2.5"
                placeholder="Password"
                {...register("rePassword", { required: true })}
              />
              <p className="mt-2 text-sm text-purple-primary">
                {errors.rePassword && (
                  <span className="text-red-primary">
                    This field is required
                  </span>
                )}
              </p>
            </div>
            <button class="bg-purple-primary hover:bg-purple-secondary text-white font-bold w-full py-2.5 rounded-lg">
              Register
            </button>
          </form>
        </div>
      </div>
    </Layout>
  );
};

export default RegisterPage;
