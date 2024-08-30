import axios, { AxiosInstance, HttpStatusCode } from "axios";

import { apiUrl } from "@/constant/env";

interface AxiosContext {
    axios: AxiosInstance;
}

type AxiosHandler<T = unknown> = (ctx: AxiosContext) => Promise<T>;

interface ErrorMessageResponse {
    message: string;
}

export function withAxiosContext<T = unknown>(
    handler: AxiosHandler<T>,
    accessToken?: string | null,
    isAuthenticated = true
): (req) => Promise<NextResponse<T | ErrorMessageResponse>> {
    return async (req) => {
        try {
            const axiosInstance = axios.create({
                baseURL: `${apiUrl}`,
                timeout: 10000,
                headers: {
                    'Content-Type': 'application/json',
                    ...(accessToken && { 'Authorization': `Bearer ${accessToken}` })
                }
            });

            if (isAuthenticated && !accessToken) {
                return false
            }

            const response = await handler({ axios: axiosInstance });
            return response
        } catch (err: any) {
            if (err.response) {
                return NextResponse.json({
                    message: err.response?.data
                }, {
                    status: err.response.status
                });
            } else {
                return 
            }



        }
    };
}
